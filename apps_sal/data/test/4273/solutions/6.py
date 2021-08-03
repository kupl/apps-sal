n = int(input())
s = [input()[0] for _ in range(n)]
c = [s.count("M"), s.count("A"), s.count("R"), s.count("C"), s.count("H")]
ans = c[0] * c[1] * c[2]
ans += c[0] * c[1] * c[3]
ans += c[0] * c[1] * c[4]
ans += c[0] * c[2] * c[3]
ans += c[0] * c[2] * c[4]
ans += c[0] * c[3] * c[4]
ans += c[1] * c[2] * c[3]
ans += c[1] * c[2] * c[4]
ans += c[1] * c[3] * c[4]
ans += c[2] * c[3] * c[4]
print(ans)
