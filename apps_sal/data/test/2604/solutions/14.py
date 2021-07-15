from sys import stdin, stdout 
from math import sqrt

def main():
    rayon, croute = map(int, stdin.readline().split())
    nbSaus = int(stdin.readline())
    diff = rayon-croute
    total = 0
    for _ in range(nbSaus):
        x, y, r = map(int, stdin.readline().split())
        dist = sqrt(x**2+y**2)
        distMin = dist-r
        distMax = dist+r 
        if distMin>=diff and distMax>=diff and distMin<=rayon and distMax<=rayon:
            total+=1
              
        
    stdout.write(str(total)) 
    
main()
