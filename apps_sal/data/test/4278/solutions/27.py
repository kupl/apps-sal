N = int(input())
s = [sorted(input()) for i in range(N)]
s.sort()
ans = 0
for i in range(N - 1):
    if s[i] == s[i + 1]:
        start = i
        end = N - 1
        while start != end:
            center = (start + end) // 2
            if s[center] == s[i]:
                if s[center + 1] == s[i]:
                    start = center + 1
                else:
                    start = end = center
            else:
                end = center
        ans += start - i
print(ans)
