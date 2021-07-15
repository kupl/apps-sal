#!/usr/bin/env python3
k, n, w = list(map(int,input().split()))
print(max(0,int(w*(w+1)/2*k-n)))

