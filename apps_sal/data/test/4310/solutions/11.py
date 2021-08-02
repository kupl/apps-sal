list = input().split(" ")
list_n = [int(s) for s in list]
print(int(max(list_n)) - int(min(list_n)))
