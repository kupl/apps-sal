def mp():
    return map(int, input().split())


n = int(input())
s = input()
cnt = 0

for i in range(n):
    if int(s[i]) % 2 == 0:
        cnt += i + 1

print(cnt)
