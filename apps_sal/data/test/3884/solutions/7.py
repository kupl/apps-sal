"""
Created on Thu Jul 26 20:46:22 2018

@author: chirayu jain
"""
planet = int(input())
mass = int(input())
case = 0
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
for i in range(0, planet):
    if A[i] == 1 or B[i] == 1:
        case = 1
        break
if case == 0:
    temp = mass * 1.0
    temp = temp / (1.0 - 1.0 / (1.0 * B[0]))
    for i in range(planet - 1, 0, -1):
        temp = temp / (1.0 - 1.0 / (A[i] * 1.0))
        temp = temp / (1.0 - 1.0 / (B[i] * 1.0))

    temp = temp / (1.0 - 1.0 / (A[0] * 1.0))
    temp = temp - mass * 1.0
if case == 1:
    print("-1")
else:
    print(temp)
