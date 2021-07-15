n, m = list(map(int, input().split()))
pu = [input() for i in range(n)]
cors = []
res = True
for string in pu:
    if "X" in string:
        if not len(cors):
            cors = string.find("X"), string.rfind("X")
        res = res and string.count("X") == (cors[1] - cors[0] + 1) and string[cors[0]:cors[1] + 1] == "X" * (cors[1] - cors[0] + 1)
if res:
    print("YES")
else:
    print("NO")

