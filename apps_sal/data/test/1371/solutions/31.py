from scipy.special import comb
S=int(input());print(sum(comb(S-2*i-3,i,1)for i in range(S//3))%(10**9+7))
