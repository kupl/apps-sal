#parse_int = list(map(int, input().split()))

lines, ppl = list(map(int, input().split()))

bus = [ [2*i-1, 2*lines+2*i-1, 2*lines+2*i,  2*i] for i in range(1, lines+1) ]

#for line in bus: print(line)

#for line in bus: exit_bus.append([ line[1], line[0], line[2], line[3] ])
for line in bus: line[1], line[0] = line[0], line[1]

exit_seq = [man for line in bus for man in line if man<=ppl]

for _ in exit_seq[:len(exit_seq)-1]:
    print(_, end=' ')
print(exit_seq[-1])
