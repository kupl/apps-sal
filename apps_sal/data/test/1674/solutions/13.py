import sys
input = sys.stdin.readline

n, k = map(int, input().split())

l = list(map(int, input().split()))

s = input()
s += "*"

summ = sum(l)
l.append(999999999999)

count = 1
temp = [l[0]]
for i in range(n):
    if s[i] == s[i + 1]:
        count += 1
        temp.append(l[i + 1])
    else:
        if count > k:
            temp.sort()
            for j in range(count - k):
                summ -= temp[j]
        temp = [l[i + 1]]
        count = 1

print(summ)
