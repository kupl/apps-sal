s = input()

se = set()
for _ in range(51):
    se.add(s)
    sl = s[1:]
    s =  sl + s[0]
print(len(se))
