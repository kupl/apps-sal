from sys import stdin as fin, setrecursionlimit as srl
# fin = open("hcc2016d1.in", "r")
debug = False


def process():
    r, c = list(map(int, fin.readline().split()))
    emp = [True] * c
    for j in range(r):
        row = fin.readline().rstrip()
        for i in range(c):
            if row[i] == 'B':
                emp[i] = False
    prev, cnt = True, 0
    for i in range(c):
        if prev and not emp[i]:
            cnt += 1
        prev = emp[i]
    print(cnt)


# fin.readline()
# process()
if not debug:
    process()
else:
    while fin.readline().strip() == '':
        process()
        print("----------------------------")
