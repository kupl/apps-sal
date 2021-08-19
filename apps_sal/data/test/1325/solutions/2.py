#fin = open("input.txt")
n, p = list(map(int, input().split()))
s = input().rstrip()
#n, p = map(int, fin.readline().split())
#s = fin.readline().rstrip()
p = min(p, n - p + 1)
Count = 0
M = l = r = X = p
for i in range(0, n // 2):
    #print(abs(ord(s[i]) - ord(s[-i - 1])), abs(ord('z') - max(ord(s[i]), ord(s[-i - 1])) + min(ord(s[i]), ord(s[-i - 1]) - ord('a') + 1) % 26), i)
    C = min(abs(ord(s[i]) - ord(s[-i - 1])), abs(ord('z') - max(ord(s[i]), ord(s[-i - 1])) + min(ord(s[i]), ord(s[-i - 1])) - ord('a') + 1) % 26)
    if C > 0:
        if (i + 1 < p):
            if (M == p):
                M = i + 1
            l = i + 1
        elif (i + 1 > p and r == p):
            r = i + 1
        X = i + 1
    Count += C
# print(Count)
#print(M, l, r, min(X * 2 - p - M, X + p - M * 2))
#print(X * 2 - p - M, X + p - M * 2)
print(Count + min(abs(X - p) + X - M, X + p - M * 2))
