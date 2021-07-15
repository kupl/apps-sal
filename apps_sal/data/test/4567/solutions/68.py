# coding = SJIS

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))

s.sort()

if sum(s) % 10 != 0:
    print(sum(s))
    return
else:
    for i in s:
        if i % 10 != 0:
            print(sum(s) - i)
            return

print(0)
