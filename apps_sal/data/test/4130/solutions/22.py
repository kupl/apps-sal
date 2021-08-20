n = int(input())
A = sorted(map(int, input().split()))
SET = set()
for a in A:
    if a == 1:
        if not 1 in SET:
            SET.add(1)
        else:
            SET.add(2)
    elif not a - 1 in SET:
        SET.add(a - 1)
    elif not a in SET:
        SET.add(a)
    else:
        SET.add(a + 1)
print(len(SET))
