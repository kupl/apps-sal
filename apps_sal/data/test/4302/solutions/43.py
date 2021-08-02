l = input().rstrip().lstrip().split(" ")
print(max(int(l[0]), int(l[1])) + max(min(int(l[0]), int(l[1])), max(int(l[0]), int(l[1])) - 1))
