z = int(input())

def sm(x):
    ans = 0
    while x>0:
        ans += x%10
        x //= 10
    return ans

for _ in range(z):
    n, s = list(map(int, input().split()))
    ans = 10000000000000000000000000000
    if sm(n) <= s:
        print(0)
        continue
    goal = n
    for i in range(len(str(n))+1):
        goal = int(str(n)[:len(str(n))-i] + '0'*i) + 10**i
        if sm(goal) <= s:
            ans = min(ans, goal-n)
    print(ans)

