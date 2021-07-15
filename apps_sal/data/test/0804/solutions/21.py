s = input()
n = int(input())
if len(s) < n:
    print("impossible")
else:
    letters = set()
    for x in s:
        letters.add(x)
    print(max(0, n - len(letters)))
