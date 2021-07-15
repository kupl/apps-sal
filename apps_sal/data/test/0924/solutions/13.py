def gcd(a, b):

    if b==0: return a
    return gcd(b, a%b)

def lucky(l_a, r_a, t_a, l_b, r_b, t_b):

    if r_b - l_b > r_a - l_a:

        thing = [l_a, r_a, l_b, r_b]

        l_a = thing[2];
        r_a = thing[3]
        l_b = thing[0]
        r_b = thing[1]

    if l_a == l_b or r_a == r_b:

        return r_b - l_b + 1

    else:

        gcdt = gcd(t_a, t_b)

        M = gcdt - ((l_a-l_b)%gcdt) ## min((l_a-l_b)%gcdt, gcdt - (l_a-l_b)%gcdt)
        if M%gcdt == 0: M=0
        ##print('M: ', M)
        overhang = max(M + (r_b - l_b + 1) - (r_a - l_a + 1), 0)
        ##print('Overhang: ', overhang)
        overlap = max(r_b - l_b + 1 - overhang, 0)
        ##print('Overlap: ', overlap)

        N = gcdt - ((r_b-r_a)%gcdt) ## min((r_a-r_b)%gcdt, gcdt - (r_a-r_b)%gcdt)
        if N%gcdt == 0: N=0
        overhang = max(0, N + (r_b - l_b + 1) - (r_a - l_a + 1))
        overlap = max(overlap, max(0, r_b - l_b + 1 - overhang))

        ##print(M, N, ((l_a-l_b)%gcdt))
    
        return overlap
    
while True:
    
    A = input().split()

    l_a = int(A[0])
    r_a = int(A[1])
    t_a = int(A[2])

    B = input().split()

    l_b = int(B[0])
    r_b = int(B[1])
    t_b = int(B[2])

    print(lucky(l_a, r_a, t_a, l_b, r_b, t_b))

    break

## stress test

##for l_a in range(0, 10):
##    for r_a in range(l_a, 10):
##        for t_a in range(max(2, r_a+1), 10):
##            for l_b in range(0, 10):
##                for r_b in range(l_b, 10):
##                    for t_b in range(max(2, r_b+1), 10):
##
##                        program_answer = lucky(l_a, r_a, t_a, l_b, r_b, t_b)
##
##                        if r_a - l_a + 1 >= t_a or r_b - l_b + 1 >= t_b: continue
##
##                        max_overlap = 0
##                        current_overlap = 0
##
##                        for i in range(0, 100):
##
##                            if i%t_a >= l_a and i%t_a <= r_a and i%t_b >= l_b and i%t_b <= r_b:
##
##                                current_overlap += 1
##
##                            else:
##
##                                current_overlap = 0
##
##                            max_overlap = max(max_overlap, current_overlap)
##
##                        if max_overlap != program_answer:
##
##                            print(program_answer)
##                            print(l_a, r_a, t_a, l_b, r_b, t_b)
                            


