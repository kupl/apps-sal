import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline()[:-1]
mod = 10**9 + 7
def readInt():return int(input())
def readIntList():return list(map(int,input().split()))
def readStringList():return list(input())
def readStringListWithSpace():return list(input().split())
def readString():return input()

n = readInt()
text = readStringList()
import collections
c  = collections.Counter(text)
if c['W'] == 0:
    print("0")
    return
i,j,count = 0,len(text)-1,0

while i <= j and i < len(text):
    if text[i] == 'W':
        while text[j] != 'R' and j > 0:
            j -= 1
        if i <= j and j > 0:
            text[i],text[j] = text[j],text[i]
            count += 1
    i += 1
print(count)


