s = input()
ans = s.count("B")
ans = min(ans, s.count("u") // 2)
ans = min(ans, s.count("l"))
ans = min(ans, s.count("b"))
ans = min(ans, s.count("a") // 2)
ans = min(ans, s.count("s"))
#a
#u
ans = min(ans, s.count("r"))
print(ans)

