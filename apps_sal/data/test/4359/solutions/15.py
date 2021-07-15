
l = [int(input()) for i in range(5)]

mod = 10
l_div = [(10-x%10)%mod for x in l]
sub = max(l_div)


ans = sum(l)+sum(l_div)-sub
print(ans)


