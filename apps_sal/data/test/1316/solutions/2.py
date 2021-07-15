n, k = map(int, input().split())
s = input()

anslevel = 0

for c in range(ord('a'), ord('z') + 1):
    ch = chr(c)
    nowLen, level = 0, 0
    for i in s:
        if i == ch:
            nowLen += 1
            if nowLen == k:
                nowLen = 0
                level += 1
        else:
            nowLen = 0
    anslevel = max(anslevel, level)

print(anslevel)
