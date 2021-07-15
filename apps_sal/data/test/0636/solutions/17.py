__author__ = 'Hippskill'
def main():
    rdl = list(map(int,input().split()))
    rdl1 = list(map(int,input().split()))
    kl = 0
    need = []
    while rdl[1] > 0:
        current = find_min(rdl1)
        if rdl[1] - rdl1[current] >= 0:
            kl += 1
            need.append(current+1)
            rdl[1] -= rdl1[current]
        else:
            break
        rdl1[current] = 10000000
    print(kl)
    for i in need:
        if i != need[len(need)-1]:
            print(i, end = " ")
        else:
            print(i, end = "")
def find_min(vect):
    mins = 10000000000
    toOut = 0
    for i in range(len(vect)):
        if mins > vect[i]:
            mins = vect[i]
            toOut = i
    return toOut
main()
