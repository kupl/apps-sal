N=50;P,Q=divmod(int(input()),N);R=N-Q;print(N,*[P+R-1]*R+[P+R+N]*Q)
