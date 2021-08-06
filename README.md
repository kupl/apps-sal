# APPS dataset refined by SAL
APPS is a python coding competition dataset.
The original contents can be found in [here](https://github.com/hendrycks/apps).

## Refined
We (SAL, Software Analysis Laboratory) refined the original dataset as follows:
* Fill missing `input_output.json`.
* Format all solutions.
* Discard buggy codes.
* Discard C++ solutions.

## Installation
You can install `apps-sal` using `pip3`.

### Requirement
`apps-sal` requires python 3.7 or higher.

### Installation
You can install `apps-sal` using `pip` and `git`.

#### Latest Released Version
Currently, the latest released version is `v0.0.1`.
If you set ssh authentication with GitHub, you can install `apps-sal` by simply typing a following command:
```bash
$ [sudo] pip3 install git+ssh://git@github.com/kupl/apps-sal.git@v0.0.1
```
If you do not use ssh authentication, you can install `apps-sal` with following commands:
```bash
$ git clone -b v0.0.1 https://github.com/kupl/apps-sal.git
$ cd apps-sal
apps-sal $ [sudo] pip3 install .
```

#### Currently Developing Version
Instead of installing latest released version, you can install currently developing snapshot in a similar way.
Use follo
```bash
$ [sudo] pip3 install git+ssh://git@github.com/kupl/apps-sal.git # clone from main branch
```
Or, if you do not use ssh authentication:
```bash
$ git clone https://github.com/kupl/apps-sal.git # clone from main branch
$ cd apps-sal
apps-sal $ [sudo] pip3 install .
```

### Examples
You can load APPS train set with the following codes:
```python
import apps_sal

train = apps_sal.load_train_dataset()
```
