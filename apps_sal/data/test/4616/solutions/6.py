s = input()
(s1, s2, s3) = (s[0], s[1:-1], s[-1])
ans = s1 + str(len(s2)) + s3
print(ans)
