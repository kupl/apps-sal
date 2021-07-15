# cook your dish here
from sys import stdin

try:
    jacket, sock, money = [int(x) for x in stdin.readline().split()]
    
    if ((money - jacket) // sock) % 2 == 0:
        print("Lucky Chef")
    else:
        print("Unlucky Chef")
        
except: pass
