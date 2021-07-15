n, k = map(int, input().split())
s = list(input())
a = ord('A')
cnt = [0] * k
for ch in s:
    cnt[ord(ch) - a] += 1
print(k * min(cnt))
