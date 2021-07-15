n , k = list(map(int,input().split()))
ai = list(map(int,input().split()))
ai.sort()
num = n // 2
num2 = num
ans = ai[num]
n2 = n - 1
while num != n2 and k > 0:
    num += 1
    k -= (ai[num] - ai[num-1]) * (num - num2)
if k < 0:
    print(ai[num] + k // (num - num2))
else:
    print(ai[num] + k // (num - num2 + 1))

