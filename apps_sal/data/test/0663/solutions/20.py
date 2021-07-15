__author__ = 'Hippskill'
import math
def main():
    rdl = list(map(int,input().split()))
    way = math.sqrt((max(rdl[1],rdl[3])-min(rdl[1],rdl[3]))**2+(max(rdl[4],rdl[2])-min(rdl[2],rdl[4]))**2)
    rdl[0] = rdl[0]*2
    print(math.ceil(way/rdl[0]))
main()
