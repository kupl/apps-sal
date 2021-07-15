import heapq as pq

from sys import stdin, stdout



#Heap method written by Engineermind.cho

#Testing if heap + fast IO can make python pass this question



n, q = list(map(int, stdin.readline().split()))

server = [i for i in range(1, n+1)]

running = []

is_chg = False

for x in stdin.readlines():

    t, k, d = list(map(int, x.split()))



    while running:

        if t >= running[0][0]:

            server += pq.heappop(running)[1]

            is_chg = True

        else:

            break



    if is_chg:

        server = sorted(server)

        is_chg = False



    if len(server) < k:

        stdout.write('-1\n')

        continue

    else:

        stdout.write(str(sum(server[:k]))+'\n')

        if d != 1:

            pq.heappush(running, (t+d, server[:k].copy()))

            server = server[k:]



# Made By Mostafa_Khaled

