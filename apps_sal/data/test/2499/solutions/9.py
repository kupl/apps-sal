n = int(input())
as_list = input().split(" ")
a_list = [ int(astr) for astr in as_list ]

x = 0

for a in a_list:
    x ^= a
for i in range(n):
    a_list[i] &= ~x
pos = 0

for b in range(59,-1,-1):

    for i in range(pos,n):
        a = a_list[i]
        if a & (1 << b):
            if i > pos:
                
                # i番目とpos番目を入れ替える
                a_list[i] = a_list[pos]
                a_list[pos] = a

            for j in range(n):
                if j == pos:
                    continue
                if a_list[j] & (1 << b):
                    a_list[j] ^= a
            pos += 1
            break
    
y = 0

for a in a_list:
    y ^= a

print((x + 2 * y))

