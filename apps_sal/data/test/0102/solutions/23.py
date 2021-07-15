import math
import functools

n = int(input())
dig = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

if n == 0:
    print("zero");
    return

if n<=10:
    print((dig[n-1]));
    return


if n == 11:
    print("eleven")

if n == 12:
    print("twelve")

if n == 13:
    print("thirteen")

if n == 14:
    print("fourteen")

if n == 15:
    print("fifteen")

if n == 16:
    print("sixteen")

if n == 17:
    print("seventeen")

if n == 18:
    print("eighteen")

if n == 19:
    print("nineteen")


ar = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];

if n>=20:
    low = n%10
    high = n//10
    if low!=0:
        print(ar[high-2]+"-"+dig[low-1])
    else:
        print(ar[high-2])
    return

