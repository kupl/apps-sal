def scanf(obj=list, type=int):
    return obj(list(map(type, input().split())))


s1 = input()
s2 = input()
for i in range(1, min(len(s1), len(s2)) + 1):
    if i == min(len(s1), len(s2)) and s1[-i] == s2[-i]:
        i += 1
        break
    if s1[-i] != s2[-i]:
        break
print(len(s1) + len(s2) - 2 * i + 2)
