moji = list(map(str, input().strip()))
print(("No", "Yes")[len(set(moji)) == 3])
