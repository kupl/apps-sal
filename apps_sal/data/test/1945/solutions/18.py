def main():
    q = int(input())
    users = []
    newusers = []
    for i in range(q):
        line = input().rstrip().split()
        old = line[0]
        new = line[1]
        if old not in newusers:
            users.append(old)
            newusers.append(new)
        else:
            index0 = newusers.index(old)
            newusers[index0] = new
    print(str(len(users)))
    for j in range(len(users)):
        print(users[j] + ' ' + newusers[j])


main()
