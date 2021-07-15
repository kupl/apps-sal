n = int(input())
s = '?' + input()
print((sum(s[i-1] != s[i] for i in range(1, len(s)))))

