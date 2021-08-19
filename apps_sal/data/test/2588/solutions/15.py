t = int(input())
for _ in range(t):
    (n, pipeCost, pillarCost) = map(int, input().split())
    road = input()
    cost = 0
    freq = []
    curr = '0'
    currFreq = 0
    for i in road:
        if i == curr:
            currFreq += 1
        else:
            freq.append(currFreq)
            curr = i
            currFreq = 1
    freq.append(currFreq)
    if len(freq) == 3:
        cost += pillarCost * freq[0]
        cost += pillarCost * 2 * (freq[1] + 1)
        cost += pillarCost * freq[2]
        cost += pipeCost * (sum(freq) + 2)
    elif len(freq) == 1:
        cost += pillarCost * (freq[0] + 1)
        cost += pipeCost * freq[0]
    else:
        level = True
        switch = 0
        cost += pipeCost * sum(freq)
        for i in range(len(freq)):
            if i % 2 == 0:
                if level:
                    if i == 0 or i == len(freq) - 1:
                        cost += pillarCost * freq[i]
                    else:
                        cost += pillarCost * (freq[i] - 1)
                elif i == len(freq) - 1:
                    level = True
                    cost += pillarCost * freq[i]
                elif (freq[i] - 1) * pillarCost > 2 * pipeCost:
                    level = True
                    cost += pillarCost * (freq[i] - 1)
                else:
                    cost += pillarCost * 2 * (freq[i] - 1)
            elif level:
                level = False
                switch += 1
                cost += pillarCost * 2 * (freq[i] + 1)
            else:
                cost += pillarCost * 2 * (freq[i] + 1)
        cost += 2 * switch * pipeCost
    print(cost)
