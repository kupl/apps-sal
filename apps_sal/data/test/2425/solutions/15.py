Q = int(input())
A = [int(input()) for i in range(Q)]
OTHER = {2 ** i - 1 for i in range(2, 26)}
OT = [2 ** i - 1 for i in range(1, 26)]
ANSDICT = {3: 1, 7: 1, 15: 5, 31: 1, 63: 21, 127: 1, 255: 85, 511: 73, 1023: 341, 2047: 89, 4095: 1365, 8191: 1, 16383: 5461, 32767: 4681, 65535: 21845, 131071: 1, 262143: 87381, 524287: 1, 1048575: 349525, 2097151: 299593, 4194303: 1398101, 8388607: 178481, 16777215: 5592405, 33554431: 1082401}
for a in A:
    if a in OTHER:
        print(ANSDICT[a])
    else:
        for i in range(30):
            if a < OT[i]:
                print(OT[i])
                break
