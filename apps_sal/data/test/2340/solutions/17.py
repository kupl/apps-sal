t = int(input())
while t > 0:
    t = t - 1
    hn = input().split()
    h = int(hn[0])
    n = int(hn[1])
    pos = input().split()
    pos = [int(val) for val in pos]
    curr = h
    curr_pos = 1
    no_crystal = 0
    while(curr > 2):
        if curr_pos >= len(pos):
            break
        if (curr - 1) == pos[curr_pos]:
            if(curr_pos == (len(pos) - 1) or (curr - 2) != pos[curr_pos + 1]):
                no_crystal = no_crystal + 1
                curr = curr - 2
                curr_pos = curr_pos + 1
            else:
                curr_pos = curr_pos + 2
        else:
            curr = pos[curr_pos] + 1
    print(no_crystal)
