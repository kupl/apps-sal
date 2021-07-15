#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL)

ll n, s;
ll e[5000];

ll increased(ll s) {
    int s2 = s;
    int digSum = 0;
    while (s > 0) {
        digSum += s % 10;
        s /= 10;
    }
    return s2 + (ll)pow(digSum, 3);
}

ll f(ll s, int i) {
    if (i == n) {
        return 0LL;
    }
    return max( f(increased(s), i+1) , f(s, i+1)+s*e[i]);
}

int main() {
    
    fastIO;
    
    cin >> n >> s;
    for (int i=0; i<n; i++) {
        cin >> e[i];
    }
    
    ll ans = f(s, 0);
    cout << ans;
    
	return 0;
}

