def judge(i):
    return "Bob" if cnt[i] > n // 2 else "Alice"


n = int(input())
a = list(map(int, input().split()))
cnt = [0 for i in range(51)]
for i in a:
    cnt[i] += 1
print(judge(min(a)))
