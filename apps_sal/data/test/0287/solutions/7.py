#!/bin/python3

import sys
n,k=map(int,input().split())
if k!=0:
    print (str(min(1,n-k)),str(min(2*k,n-k)))
else:
    print ("0 0")
