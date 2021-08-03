s = input()
T = 'AEFHIKLMNTVWXYZ'
ok1 = 1
ok2 = 1
for i in s:
    if i not in T:
        ok1 = 0
    else:
        ok2 = 0
print(["NO", "YES"][ok1 or ok2])
