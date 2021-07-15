__author__ = 'default'
def TaskA():
    #fl = open('TaskA.txt','r')
    n, m, k = list(map(int,input().split()))
    pole = [0]*n
    lose = False
    cmplt = True
    for i in range(n):
        pole[i] = [0]*m
    for i in range(k):
        rdl = list(map(int,input().split()))
        pole[rdl[0]-1][rdl[1]-1] = 1
        lose = check(pole, rdl[0]-1,rdl[1]-1)
        if lose and cmplt:
            cmplt = False
            print(i+1)
    #fl.close()
    if not lose and cmplt:
        print(0)
def check(pole, index1,index):
    if index1-1 >= 0 and index+1 < len(pole[0]):
        if pole[index1][index+1] == 1 and pole[index1-1][index] == 1 and pole[index1-1][index+1] == 1:
            return True
    if index1+1 < len(pole) and index-1>0  >= 0:
        if pole[index1][index-1] == 1 and pole[index1+1][index-1] == 1 and pole[index1+1][index] == 1:
            return True
    if index1-1 >= 0 and index-1 >= 0:
        if pole[index1-1][index] == 1 and pole[index1-1][index-1] == 1 and pole[index1][index-1] == 1:
            return True
    if index1+1 < len(pole) and index+1 < len(pole[0]):
        if pole[index1+1][index] == 1 and pole[index1+1][index+1] == 1 and pole[index1][index+1]:
            return True

TaskA()
