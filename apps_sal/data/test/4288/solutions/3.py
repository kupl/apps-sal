import os, sys, re, math

(A, B, C) = [int(n) for n in input().split()]

if (A == B and B != C) or (A == C and A != B) or (B == C and A != B):
    print('Yes')
else:
    print('No')

