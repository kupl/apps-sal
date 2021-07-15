for repeat in range(int(input())):
    studentsnum = int(input())
    res = ""
    laststudent = 0
    for i in range(studentsnum):
        inp = input().split(" ", 1)
        arrival = int(inp[0])
        departure = int(inp[1])
        if arrival > laststudent:
            laststudent = arrival
        if departure < laststudent:
            res = res + str(0) + " "
        else:
            res = res + str(laststudent) + " "
            laststudent = laststudent + 1
    print(res)
            

