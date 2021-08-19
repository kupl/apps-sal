isPrime = [1 for i in range(1000005)]
primes = []
for i in range(2, 1000005):
    if isPrime[i] == 1:
        primes.append(i)
        j = 2 * i
        while j < 1000005:
            isPrime[j] = 0
            j += i


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


t = int(input())
while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    ans = 1
    flag = 1
    for i in range(len(d) - 1):
        if d[i] * d[n - i - 1] != d[i + 1] * d[n - i - 2]:
            flag = 0
            break
    if flag == 0:
        print(-1)
    else:
        ans = d[0] * d[-1]
        amt = 1
        x = ans
        for i in primes:
            if ans % i == 0:
                cnt = 1
                while x % i == 0:
                    cnt += 1
                    x /= i
                amt *= cnt
        if x > 1:
            amt *= 2
        if amt - 2 == len(d):
            print(int(ans))
        else:
            print(-1)
    '    \n    for i in d:\n        ans=lcm(ans,i)\n        if(ans>10**30):\n            print(-1)\n            break\n    if(ans>10**30):\n        t-=1\n        continue \n    if(ans==d[-1]):\n        po=1\n        flag=1\n        for i in d:\n            po*=d[0]\n            if(po!=i):\n                flag=0\n        if(flag==1):\n            print(int(ans*d[0]))\n        else:\n            print(-1)\n    else:\n        amt=1\n        x=ans\n        for i in primes:\n            if(ans%i==0):\n                cnt=1\n                while(x%i==0):\n                    cnt+=1\n                    x/=i\n                amt*=cnt\n        if(x>1):\n            amt*=2\n        if(amt-2==len(d)):\n            print(int(ans))\n        else:\n            print(-1)\n    '
    t -= 1
