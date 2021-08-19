'''
           _                              _    
          | |                            | |   
 ___ _   _| |__   ___ _ __ __ _  ___  ___| | __
/ __| | | | '_ \ / _ \ '__/ _` |/ _ \/ _ \ |/ /
\__ \ |_| | |_) |  __/ | | (_| |  __/  __/   < 
|___/\__, |_.__/ \___|_|  \__, |\___|\___|_|\_\
      __/ |                __/ |               
     |___/                |___/                
'''
n = int(input())
a = list(map(int, input().split()))

pa = []
sa = []
a.sort()
for i in range(n):
    if i % 2 == 0:
        pa.append(a[i])
    else:
        sa.append(a[i])
sa.reverse()
resa = pa + sa
# print(resa)
for i in resa:
    print(i, end=' ')
