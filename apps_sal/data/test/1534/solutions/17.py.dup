str = input()
l = len(str)
ok = 0
test1 = 0
test2 = 0
for i in range(l):
    if(str[i] == 'a'):
        ok = ok + 1
        test2 = max(test1 + 1, test2 + 1)
    else:
        test1 = max(test1 + 1, ok + 1)
print(max(test1, test2))
