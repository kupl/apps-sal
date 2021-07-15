#!/bin/python3

import sys
a = input()
b = input()
if  a == b:
    print(-1)
    return
print(max(len(a),len(b)))
