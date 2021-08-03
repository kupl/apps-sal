#!/usr/bin/env python3

# import
#import math
#import numpy as np
K = int(input())
S = input()

print((S[:min(len(S), K)] + ("..." if len(S) > K else "")))
