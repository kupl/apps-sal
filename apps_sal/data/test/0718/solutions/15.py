import sys
for line in sys.stdin.readlines() :
    num = int(line.strip())
    for i in range(1,8888888889-num) : 
        if str(num+i).count('8') : 
            print(i)
            break
    break

